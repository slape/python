#!/usr/bin/env python3

def gather():
    flag_list = {}
    while True:
        flag = input('Enter the flag: ')
        if flag == 'q':
            break
        desc = input('Enter the description: ')
        flag_list[flag] = desc
    return flag_list

def print_(flag_list):
    out = f'<details>\n  <summary>Expand for Explanations of Flags</summary>\n  <ul>'
    for flag, desc in flag_list.items():
        out += f'\n    <li><code>{flag}</code>: {desc}.'
    out += f'\n  </ul>\n</details>'
    print(out)


def main():
    flag_list = gather()
    print_(flag_list)

if __name__ == "__main__":
    main()