import json
import subprocess


def create_accounts(domain, username, password):
    cmd = "ejabberdctl register {} {} {}".format(username, domain, password)
    print(cmd)
    subprocess.call(cmd)


def forge_relations(user1,user2,domain):
    cmd1 = "ejabberdctl add-rosteritem {} {} {} {} {}-{} groupvpn both"\
            .format(user1,domain,user2,domain,user1,user2)
    cmd2 = "ejabberdctl add-rosteritem {} {} {} {} {}-{} groupvpn both" \
        .format(user2, domain, user1, domain, user2, user1)
    print("\n")
    print(cmd1)
    print(cmd2)
    subprocess.call(cmd1)
    subprocess.call(cmd2)

with open('friends.json') as json_file:
    data = json.load(json_file)
    domain = data["domain"]
    for node in data['relations']:
        create_accounts(domain, node, node)
    for node in data["relations"]:
        friends = data["relations"][node]
        for friend in friends:
            forge_relations(node,friend,domain)