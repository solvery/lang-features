import ldap

try:
    l = ldap.open("127.0.0.1")
    l.protocol_version = ldap.VERSION3    
except ldap.LDAPError, e:
    print e

## The next lines will also need to be changed to support your search requirements and directory
baseDN = "cn=Manager,dc=example,dc=com"
searchScope = ldap.SCOPE_SUBTREE
## retrieve all attributes - again adjust to your needs - see documentation for more options
retrieveAttributes = None 
searchFilter = "cn=*"

try:
    ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
    result_set = []
    while 1:
        result_type, result_data = l.result(ldap_result_id, 0)
        if (result_data == []):
            break
        else:
            ## here you don't have to append to a list
            ## you could do whatever you want with the individual entry
            ## The appending to list is just for illustration. 
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    print result_set
except ldap.LDAPError, e:
    print e
