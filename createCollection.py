import subprocess


def createCollection(p_collection_name):

    solr_path = r"E:\DoNotDelete\Downloads\solr-8.11.4\bin"

    solr_command = "solr start"
    core_command = f"solr create -c {p_collection_name}"
    list_collections_command = "solr list"

    try:
        ping_result = subprocess.run("solr status", shell=True, cwd=solr_path, capture_output=True, text=True)

        if "not running" in ping_result.stdout:
            print("Solr is not running. Starting Solr...")
            cmd_output = subprocess.run(solr_command, shell=True, cwd=solr_path, capture_output=True, text=True)

            if output.returncode == 0:
                print("Solr started successfully.")
            else:
                print("Error starting Solr.")
                print("Error message:\n", cmd_output.stderr)
        else:
            print("Solr is already running.")

    except Exception as e:
        print("An error occurred while checking Solr status:", e)

    try:
        list_result = subprocess.run(list_collections_command, shell=True, cwd=solr_path, capture_output=True, text=True)

        cmd_output= subprocess.run(core_command, shell=True, cwd=solr_path, capture_output=True, text=True)

        if cmd_output.returncode == 0:
            print(f"Collection {p_collection_name} created successfully.")
        else:
            print(f"Error creating collection {p_collection_name}.")
            print("Error message:\n", cmd_output.stderr)

    except Exception as e:
        print("An error occurred while checking or creating the collection:", e)

v_nameCollection = "Hash_Bala_Krishna"
v_phoneCollection = "Hash_7700"

createCollection(v_nameCollection)
createCollection(v_phoneCollection)
