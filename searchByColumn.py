import pysolr

def searchByColumn(p_collection_name,p_column_name, p_column_value):
    solr_link = f'http://localhost:8989/solr/{p_collection_name}'

    solr = pysolr.Solr(solr_link)

    query = f'{p_column_name}:{p_column_value}'
    results = solr.search(query)

    for result in results:
        print(result)

v_nameCollection = "Hash_Bala_Krishna"

v_phoneCollection = "Hash_7700"

p_column_name ='Department'
p_column_value = 'IT'

searchByColumn(v_nameCollection,p_column_name,p_column_value)

searchByColumn(v_phoneCollection,p_column_name,p_column_value)
