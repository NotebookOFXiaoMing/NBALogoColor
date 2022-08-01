import yaml
import argparse
import pkg_resources

def load_nbalogo_color():
    stream = pkg_resources.resource_stream(__name__,'data/nba_logo.yml')
    #nbalogocolor = {}
    #with open(stream,'r') as file:
    documents = yaml.full_load(stream.read())
        
    return documents

def load_nbateam_name():
    color_dict = load_nbalogo_color()
    return color_dict.keys()

def pick_teams_color(team):
    if team not in load_nbateam_name():
        print("Maybe the team's name is spelled wrong.")
        print("You can get all team names by running load_nbateam_name() function.")
    else:
        print(load_nbalogo_color()[team])
        
def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="get nba team logo color",
        epilog='''
        @author: MingYan
        @contact: mingyan24@126.com
        '''
    )
    
    parser.add_argument("-t",'--team-name',required=True,help="specify the team name")
    
    args = parser.parse_args()
    
    pick_teams_color(args.team_name)
    

def main02():
    print(load_nbateam_name())
