
LDAP_HOST = '192.168.0.9'

def ldap_getcn(username):
    try:
        l = ldap.open(LDAP_HOST)
        l.protocol_version = ldap.VERSION3
        l.simple_bind(LDAP_BIND, LDAP_PASS)

        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = "uid=*" + username + "*"
        resultID = l.search(LDAP_BASE, searchScope, searchFilter, None)
        result_set = []
        while 1:
            result_type, result_data = l.result(resultID, 0)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
        return result_set[0][0][1]['cn'][0]
    except ldap.LDAPError, e:
        print e
