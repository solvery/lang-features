#include "unp.h"
#include "myerror.h"
#include <stdio.h>
#include <string.h>
#include <sys/select.h>

#define PORT 8687
#define BUFSIZE 1000

int max(int a, int b){
    return a>b?a:b;
}

int main(int argc, char* argv[]){
    int sockfd;
    int stdinfd;
    int maxfdp1;
    fd_set fdset;
    struct sockaddr_in addr;
    char buf[BUFSIZE];

    stdinfd = fileno(stdin);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_port = htons(PORT);

    //connect to server
    if(connect(sockfd, (struct sockaddr*)&addr, sizeof(addr)) == -1){
        errMsg("connect");
        exit(-1);
    }

    for(;;){
        FD_ZERO(&fdset);
        FD_SET(stdinfd, &fdset);
        FD_SET(sockfd, &fdset);
        maxfdp1 = max(stdinfd, sockfd) + 1;
        select(maxfdp1, &fdset, NULL, NULL, NULL);
        int n;
        int len;
        if(FD_ISSET(sockfd, &fdset)){
            //printf("read from peer ready\n");
            if((n = readn(sockfd, buf, len))== -1){
                errMsg("readn");
                exit(-1);
            }
            else if(n == 0){
                printf("server closed\n");
                exit(0);
            }
            printf("%s", buf);
        }

        if(FD_ISSET(stdinfd, &fdset)){
            if(fgets(buf, BUFSIZE, stdin) == NULL){
                exit(0);
            }
           len = strlen(buf) + 1;
           //printf("read %d bytes from stdin\n", len);
           writen(sockfd, buf, len);
           //printf("write to peer\n");
        }
    }
}
