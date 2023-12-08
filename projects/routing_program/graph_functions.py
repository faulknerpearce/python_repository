from bfs import bfs
from dfs import dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices
from message_delay import delayed_print, delayed_input

# Creates a formatted string listing landmarks and their corresponding letters.
def create_landmark_string(landmarks_dict):
   landmark_str =''
   for letter, landmark in landmarks_dict.items():
      landmark_str += f"{letter} - {landmark}\n"
   return landmark_str

# Displays a welcome message for the SkyRoute application.
def greet(landmarks_str):
  delayed_print('\nHi there and welcome to SkyRoute!')
  delayed_print(f"We'll help you find the shortest route between the following Vancouver landmarks:\n")
  print(landmarks_str)

# Displays a goodbye message for the SkyRoute application.
def goodbye():
   delayed_print('\nThanks for using SkyRoute!')

# Shows the list of landmarks again based on user input.
def show_landmarks(landmarks_str):
   see_landmarks = delayed_input('\nWould you like to see the list of landmarks again? Enter y for Yes and n for No: ')

   if see_landmarks.lower() == 'y':
      print(f'\n{landmarks_str}')
   
   elif see_landmarks == 'n':
      delayed_print('\nOk, we wont the list of landmarks. ')

   else:
      delayed_print('\nInvailid input, please try again.')
      show_landmarks(landmarks_str)

# Retrieves the user's input for the starting point of the route.
def get_start():
    start_point_letter = delayed_input("\nWhere are you coming from? Type in the corresponding letter: ")

    if start_point_letter in landmark_choices:
        start_point = landmark_choices[start_point_letter]
        return start_point

    else:
        delayed_print("\nSorry, that's not a landmark we have data on. Let's try this again.")
        return get_start()

# Retrieves the user's input for the ending point of the route.
def get_end():
   end_point_letter = delayed_input("\nwhere are you headed? Type in the corresponding letter: ")

   if end_point_letter in landmark_choices:
      end_point = landmark_choices[end_point_letter]
      return end_point
   
   else:
      delayed_print("\nSorry, that's not a landmark we have data on. Let's try this again.")
      return get_end()

# Returns an updated metro dictionary with stations under construction removed from neighboring stations. 
def get_active_stations(vc_metro_dict, the_stations_under_construction):
   
   updated_metro = vc_metro_dict

   for station_under_construction in the_stations_under_construction:
      for current_station, neighboring_stations in vc_metro_dict.items():
         if current_station != station_under_construction:
            updated_metro[current_station] -= set(the_stations_under_construction)
         else:
            updated_metro[current_station] = set([])
   return updated_metro

# Sets the starting and ending points for the route, allowing the user to change them if needed.
def set_start_and_end(start_point, end_point, landmarks_str):
    if start_point is not None:
        change_point = delayed_input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print("Oops, that isn't 'o', 'd', or 'b'.")
            return set_start_and_end(start_point, end_point, landmarks_str)
    else:
        start_point = get_start()
        end_point = get_end()

    return start_point, end_point

# Finds the shortest route between two landmarks using breadth first search.
def get_route(start_point, end_point, vc_landmarks_dict, vc_metro_dict, construction):
    
   start_stations = vc_landmarks_dict[start_point]
    
   end_stations = vc_landmarks_dict[end_point]
   routes = []

   for start_station in start_stations:
    
       for end_station in end_stations:
          metro_system = get_active_stations(vc_metro_dict, construction) if construction else vc_metro_dict
          if len(construction) > 0:
             possible_route = dfs(metro_system, start_station, end_station)
             if possible_route is None:
               return None
          
          route = bfs(metro_system, start_station, end_station)
          if route is not None:
             routes.append(route)

   shortest_route = min(routes, key=len)
   return shortest_route

# Displays the shortest route and asks the user if they want to see another route.
def new_route(landmarks_str, vc_landmarks_dict, vc_metro_dict, construction, start_point=None, end_point=None):
   
   the_start_point, the_end_point = set_start_and_end(start_point, end_point, landmarks_str)
   shortest_route = get_route(the_start_point, the_end_point, vc_landmarks_dict, vc_metro_dict, construction)

   if shortest_route is not None:
   
      shortest_route_string = '\n'.join(shortest_route)

      delayed_print(f'\nThe shortest metro route from {the_start_point} to {the_end_point} is:\n\n{shortest_route_string}')
   
   else:
      delayed_print(f'Unfortunately, there is currently no path between {the_start_point} and {the_end_point} due to maintenance.')


   again = delayed_input('\nWould you like to see another route? Enter y for Yes and n for No: ')

   if again.lower() == 'y':
      show_landmarks(landmarks_str)
      new_route(landmarks_str, vc_landmarks_dict, vc_metro_dict, the_start_point, the_end_point)

# Initiates the SkyRoute application.          
def skyroute(landmarks_str, vc_landmarks_dict, vc_metro_dict, construction):
  greet(landmarks_str)
  new_route(landmarks_str, vc_landmarks_dict, vc_metro_dict, construction)
  goodbye()