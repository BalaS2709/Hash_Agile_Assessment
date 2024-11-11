import pysolr

def getEmpCount(v_nameCollection):

    solr_link = f'http://localhost:8989/solr/{v_nameCollection}'
    solr = pysolr.Solr(solr_link)

    query = '*:*'
    results = solr.search(query)

    print(f"Count : {results.hits}")

v_nameCollection = "Hash_Bala_Krishna"

getEmpCount(v_nameCollection)


