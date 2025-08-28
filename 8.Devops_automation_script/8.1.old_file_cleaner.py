import os,time
def clean_old_file(path,days=30):
    now = time.time()
    cutoff = now - (days * 86400)

    for root,dirs,files in os.walk(path):
        for file in files:
            filepath = os.path.join(root,file)
            if os.path.getmtime(filepath)<cutoff:
                print(f"🗑️ Deleting the file {filepath}")
clean_old_file("/tmp",days=7)
