import sys
from parsingutils import load_n_results

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Arguments missing")
        exit()

    action = sys.argv[1]

    allowed_actions = [
        'show',
        'urlcontains',
        'title',
        'toprating'

    ]

    if action not in allowed_actions:
        print(f'Wrong action {action}')
        exit()

    if action == 'urlcontains':
        if len(sys.argv) == 4:
            _, action, limit, word = sys.argv
        elif len(sys.argv) == 3:
            limit = 50
            _, action, word = sys.argv
        else:
            print("Wrong number of arguments")
            exit()

        posts = load_n_results(int(limit))

        for p in posts:
            if word in p['url']:
                print(p['url'])

    if action == 'show':
        if len(sys.argv) == 3:
            _, action, limit = sys.argv
        else:
            print("Wrong number of arguments")
            exit()

        posts = load_n_results(int(limit))

        for p in posts:
            print(p)

    if action == 'title':
        if len(sys.argv) == 3:
            _, action, limit = sys.argv

        else:
            print("Wrong number of arguments")
            exit()

        posts = load_n_results(int(limit))

        for p in posts:
            print( p['title'], p['author'])



