#include "unp.h"
#include <stdio.h>
#include <stdlib.h>
#include "myerror.h"
#include <sys/select.h>


#define PORT 8687
#define BUFSIZE 1000

int max(int a, int b){
    return a > b? a:b;
}
void str_echo(int);

int main(int argc, char* argv[]){
    int listenfd; //server socket file descriptor
    int connfd;
    char buf[BUFSIZE];

    struct sockaddr_in servaddr;
    struct sockaddr_in connaddr;
    socklen_t connaddr_len;
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    //create a listen socket
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    if(listenfd == -1){
        errMsg("socket");
        exit(-1);
    }

    //bind
    int ret = bind(listenfd, (struct sockaddr*)&servaddr, sizeof(servaddr));
    if(ret == -1){
        errMsg("bind");
        exit(-1);
    }

    //listen
    listen(listenfd, LISTENQ);

    int clientfd[FD_SETSIZE];
    int maxi = -1;//max index of clientfd
    int i;
    for(i = 0; i < FD_SETSIZE; i++){
        clientfd[i] = -1;
    }
    fd_set fdset;
    fd_set fdreset;
    FD_ZERO(&fdset);
    FD_SET(listenfd, &fdset);
    int maxfdp1 = listenfd + 1;

    for(;;){
         fdreset = fdset;
         int nready;
         nready = select(maxfdp1, &fdreset, NULL, NULL, NULL);

         //add new connection
         if(FD_ISSET(listenfd, &fdreset)){
            connfd = accept(listenfd,(struct sockaddr*)&connaddr,&connaddr_len);
            printf("connect from %s:%d\n", inet_ntoa(connaddr.sin_addr),htons(connaddr.sin_port));
            if(connfd == -1){
                errMsg("connect");
                exit(-1);
            }
            for(i = 0; i <= maxi; i++){
                   if(clientfd[i] == -1){
                       clientfd[i] = connfd;
                       break;
                   }
             }
            if(i > maxi){
                if(i == FD_SETSIZE){
                    printf("too many connection\n");
                    exit(-1);
                }
                else{
                       maxi++;
                       clientfd[maxi] = connfd;
                }
            }
            FD_SET(connfd,&fdset);
            maxfdp1 = max(maxfdp1, connfd + 1);
            nready--;
         }
         //echo str
         for(i = 0; i <= maxi; i++){
             int n;
             if(FD_ISSET(clientfd[i], &fdreset)){
                 if((n = read(clientfd[i], buf, BUFSIZE)) == 0){
                     printf("connection closed by client\n");
                     close(clientfd[i]);
                     FD_CLR(clientfd[i], &fdset);
                     clientfd[i] = -1;
                 }
                 else{
                     writen(clientfd[i], buf, n);
                 }
                 if(--nready == 0)
                     break;
             }
         }
    }
}

/**
 * echo string to client
 */
void str_echo(int connfd){
     //read line from client
    char buf[BUFSIZE];
    int n;
again:
    while((n = read(connfd,buf,BUFSIZE)) > 0){
       //printf("read %d bytes from peer\n", n);
       int ret =  writen(connfd,buf,n);
       if(ret == -1){
           break;
       }
       //printf("write %d bytes to peer\n", ret);
    }
    if(n < 0 && errno == EINTR){//read was interrupted
        goto again;
    }
    else if(n < 0){
        errMsg("read");
    }
}

