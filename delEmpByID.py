import pysolr

def delEmpByID(p_collection_name,Emp_ID):
    solr_link = f"http://localhost:8989/solr/{p_collection_name}"
    solr = pysolr.Solr(solr_link)

    query = f'EmployeeID:{Emp_ID}'

    results = solr.delete(q=query)
    solr.commit()
    if results:
        print(f' Data Deleted for EmployeeID - {Emp_ID}')

v_nameCollection = "Hash_Bala_Krishna"


delEmpByID(v_nameCollection, 'E02003')

