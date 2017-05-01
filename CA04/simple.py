
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    
    # print the number of lines read
    print(len(data))
    #print(commits)
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))
    #print(commits[:3]['author']) # returns error
    
    index = 0
    count = 0
    name=raw_input('Enter name:')
    while index < len(commits):
        author = (commits[index]['author'])
        #print author
        authors = []
        for author in authors:
            if author not in authors:        
               authors.append(author)
        
        index = index + 1
        
        if author == name:
            count = count + 1
    per_cent = round((float(count) / len(commits)) * 100,2)
    print '{} made {} commits, which is {}% of total commits'.format(name,count,per_cent)
    print authors
    