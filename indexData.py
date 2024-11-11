import csv
import pysolr
import requests


def indexData(p_collection_name, exclude_column=None):
    solr_link = f"http://localhost:8989/solr/{p_collection_name}"
    solr = pysolr.Solr(solr_link)
    csv_file_path = 'E:/DoNotDelete/Downloads/Employee_Sample_Data_1.csv'

    documents = []
    with open(csv_file_path, newline='', encoding='latin') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            document = {
                'EmployeeID': row['Employee ID'],
                'FullName': row['Full Name'],
                'JobTitle': row['Job Title'],
                'Department': row['Department'],
                'BusinessUnit': row['Business Unit'],
                'Gender': row['Gender'],
                'Ethnicity': row['Ethnicity'],
                'Age': row['Age'],
                'HireDate': row['Hire Date'],
                'AnnualSalary': row['Annual Salary'],
                'BonusPercentage': str(row['Bonus %'].replace("%","")),
                'Country': row['Country'],
                'City': row['City'],
                'ExitDate': row['Exit Date'],
            }

            if exclude_column and exclude_column in document:
                document.pop(exclude_column)

            documents.append(document)

    solr.add(documents)
    solr.commit()

    print(f"Successfully indexed {len(documents)} documents into {p_collection_name}.")


v_nameCollection = "Hash_Bala_Krishna"
n_exclude_column = "Department"

v_phoneCollection = "Hash_7700"
p_exclude_column = "Gender"

indexData(v_nameCollection, n_exclude_column)
indexData(v_phoneCollection, p_exclude_column)
