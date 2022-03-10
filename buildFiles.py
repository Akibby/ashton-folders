import csv, os

# specify the name of the file that contains the source data
filename = "sample.csv"
# get the current directory where work is happening
cwd = os.getcwd()

# Generic subfolders that every entity gets
generic_subfolders = [["credit", "cred1", "cred2"], ["collateral", "coll1", "coll2"]]

with open(filename, 'r') as f:
    reader = csv.reader(f)
    cur_entity = ""
    for row in reader:
        # build main directory
        if row[0] != "":
          cur_entity = row[0]
          if not os.path.exists(os.path.join(cwd,cur_entity)):
            os.mkdir(os.path.join(cwd,cur_entity))
            # add subfolders to new folder
            for subfolder in generic_subfolders:
              os.mkdir(os.path.join(cwd,cur_entity,subfolder[0]))
              for sub in subfolder[1:]:
                os.mkdir(os.path.join(cwd,cur_entity,subfolder[0],sub))

        # build child directories
        # check if the child directory is already in the root and make it if not
        if not os.path.exists(os.path.join(cwd,row[1])):
          os.mkdir(os.path.join(cwd,row[1]))
          os.symlink(os.path.join(cwd,row[1]), os.path.join(cwd,cur_entity,row[1]))
          # add subfolders to new folder
          for subfolder in generic_subfolders:
            os.mkdir(os.path.join(cwd,row[1],subfolder[0]))
            for sub in subfolder[1:]:
              os.mkdir(os.path.join(cwd,row[1],subfolder[0],sub))
        # check if the child directory is already linked in the current entity and make a link if not
        elif not os.path.exists(os.path.join(cwd,cur_entity,row[1])):
          os.symlink(os.path.join(cwd,row[1]), os.path.join(cwd,cur_entity,row[1]))
