import pysolr

def getDepFacet(p_collection_name):
    solr_link = f"http://localhost:8989/solr/{p_collection_name}"
    solr = pysolr.Solr(solr_link)

    query = '*:*'
    para = {
        'facet': 'true',
        'facet.field': 'Department',
        'rows': 0
    }
    try:
        results = solr.search(query, **para)

        # Retrieve and print the facets (department counts)
        department_counts = results.facets['facet_fields'].get('Department', [])
        print("Department-wise employee count:")
        for i in range(0, len(department_counts), 2):
            department = department_counts[i]
            count = department_counts[i + 1]
            print(f"{department}: {count} employees")

    except pysolr.SolrError as e:
        print(f"Error fetching facet data: {e}")


v_nameCollection = "Hash_Bala_Krishna"
v_phoneCollection = "Hash_7700"

getDepFacet(v_phoneCollection)

