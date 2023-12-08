from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
from graph_functions import create_landmark_string, skyroute

# ________Main Program_________ #
landmark_choices_string = create_landmark_string(landmark_choices)

stations_under_construction = ['Lansdowne', 'Templeton']

skyroute(landmark_choices_string, vc_landmarks, vc_metro, stations_under_construction)
