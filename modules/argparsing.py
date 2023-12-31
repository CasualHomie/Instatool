import argparse
from modules.constants import APP_VERSION

description = " "
usage = " "
#[-le --loadenv] [-np NOOFPOSTS] [-ps TEXT] [-c FILE | -nc] [-d DELAY] [-hl --headless]"
examples=""" """
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=description,
    usage=usage,
    epilog=examples,
    prog='ilcbot')


# optional arguments
parser.add_argument('-u','--username', metavar='', type=str, help='Instagram username')
parser.add_argument('-p','--password', metavar='', type=str, help='Instagram password')
parser.add_argument('-t', '--target',  metavar='', type=str, help='target (account or tag)')

parser.add_argument('-np', '--numofposts', type=int, metavar='numposts', help='number of posts to like')
parser.add_argument('-ps', '--postscript', type=str, metavar='text', help='additional text to add after every comment')
parser.add_argument('-ff', '--findfollowers', action='store_true', help="like/comment on posts from target's followers")
parser.add_argument('-fa', '--followersamount', type=int, metavar='numfollowers', help='number of followers to process (default=all)')
parser.add_argument('-lc', '--likecomments', type=int, metavar='', help='like top n user comments per post')
parser.add_argument('-il', '--inlast', type=str, metavar='', help='target post within last n years (y), months (M), days (d), hours (h), mins (m), secs (s)')

parser.add_argument('-vs', '--viewstory', action='store_true', help='view stories')
parser.add_argument('-ls', '--likestory', type=int, nargs='?', metavar='numstories', help='like stories (default=all)')
parser.add_argument('-cs', '--commentstory', type=int, nargs='?', metavar='numcomments', help='comments on stories (no comments if option not used)')
parser.add_argument('-os', '--onlystory', action='store_true', help='target only stories and not posts')

parser.add_argument('-mr', '--mostrecent', action='store_true', help='target most recent posts')
parser.add_argument('-rr', '--reloadrepeat', type=int, metavar='times', help='reload the target n times (used with -mr)')

parser.add_argument('-mt', '--matchtags', type=str, metavar='tag_file', help='read tags to match from a file')
parser.add_argument('-it', '--ignoretags', type=str, metavar='tag_file', help='read tags to ignore from a file')
match_group = parser.add_mutually_exclusive_group()
match_group.add_argument('-mn', '--matchtagnum', type=int, metavar='count', help='minimum tag match count for post to be qualified')
match_group.add_argument('-ma', '--matchalltags', action='store_true', help='match all tags in matchtags')

comments_group = parser.add_mutually_exclusive_group()
comments_group.add_argument('-c', '--comments', type=str, metavar='file', help='file containing comments (one comment per line)')
comments_group.add_argument('-oc', '--onecomment', type=str, metavar='text', help='specify only one comment')
comments_group.add_argument('-nc', '--nocomments', action='store_true', help='turn off comments')

parser.add_argument('-load', '--profile', type=str, metavar='', help='loads profile from a json file')
parser.add_argument('-bp', '--brprofile', type=str, metavar='', help='loads chrome profile from a path')
parser.add_argument('-et', '--eltimeout',  type=int, metavar='', help='max time to wait for elements to be loaded (default=30)')
parser.add_argument('-d', '--delay', type=str, metavar='min,max', help='time to wait during post switch default=1,10')
parser.add_argument('-br', '--browser',  type=str, metavar='', choices = ('chrome', 'firefox'), help='browser to use [chrome|firefox] (default=chrome)')
parser.add_argument('-hl', '--headless',  action='store_true', help='headless mode')
parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {APP_VERSION}')
