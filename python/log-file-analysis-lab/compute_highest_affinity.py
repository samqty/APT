# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    visitlog = dict()

    for i in range(0, len(site_list)):
        if user_list[i] in visitlog:
            if site_list[i] in visitlog[user_list[i]]:
                pass
            else:
                visitlog[user_list[i]].append(site_list[i])
        else:
            visitlog[user_list[i]] = [site_list[i]]

    affinitylog = dict()
    for v in visitlog:
        for site1 in visitlog[v]:
            for site2 in visitlog[v]:
                if site1 != site2:
                    if site1 + "-" + site2 in affinitylog:
                        affinitylog[site1 + "-" + site2] += 1
                    else:
                        affinitylog[site1 + "-" + site2] = 1
                else:
                    pass

    bestaffinity = sorted(sorted(affinitylog, key=affinitylog.get, reverse=True)[0].split("-"))

    return (bestaffinity[0], bestaffinity[1])
