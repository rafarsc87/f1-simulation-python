import random

# ----------------------------
# F1 Simulation V1
# A simple terminal-based Formula 1 championship simulation.
# ----------------------------

# ----------------------------
# 1. DATA
# ----------------------------

DRIVERS = [
    {"name": "Juan Manuel Fangio", "skill": 10, "consistency": 7},
    {"name": "Michael Schumacher", "skill": 8, "consistency": 10},
    {"name": "Max Verstappen", "skill": 10, "consistency": 9}

]

TRACKS = [
    {"name": "Monaco", "difficulty": 0.8, "speed_bias": 0.2},
    {"name": "Suzuka", "difficulty": 0.75, "speed_bias": 0.8},
    {"name": "Silverstone", "difficulty": 0.6, "speed_bias": 1}
]

EXTRA_TIE_TRACK = {"name":"Nürburgring", "difficulty": 0.95, "speed_bias": 0.6}

POINTS_SYSTEM = {
    1: 25,
    2: 18,
    3: 15
}


# ----------------------------
# 2. HELPER FUNCTIONS
# ----------------------------

def calculate_driver_score(driver: dict[str, int], track: dict[str, float]) -> float:
    """
    Calculates the performance score of a single driver for a specific track.

    Args:
        driver: A dictionary containing driver attributes (skill, consistency).
        track: A dictionary containing track attributes (difficulty, speed_bias).

    Returns:
        The calculated performance score including a luck factor, rounded to 2 decimal places.
    """
    # Configuration for balance
    MIN_LUCK = -9
    MAX_LUCK = 9

    luck_factor = random.randint(MIN_LUCK, MAX_LUCK)

    # Core logic
    skill_impact = driver["skill"] * track["difficulty"]
    speed_impact = driver["consistency"] * track["speed_bias"]

    total_score = skill_impact + speed_impact + luck_factor

    # Return rounded to 2 decimal places for cleaner display
    return round(total_score, 2)
        

def run_race(drivers: list[dict[str, int]], current_track: dict[str, float]) -> list[tuple[str, float]]:
    """
    Simulates a race by calculating scores for all drivers and ranking them.

    Args:
        drivers: List of all driver dictionaries.
        current_track: The track dictionary for the current race.

    Returns:
        list: A sorted list of tuples containing (driver_name, score), sorted from winner to last place.
    """
    race_performance_map = {}

    for driver in drivers:
        score = calculate_driver_score(driver, current_track)
        race_performance_map[driver['name']] = score
        
    return rank_drivers(race_performance_map) 
    
    
def rank_drivers(race_scores: dict[str, float]) -> list[tuple[str, float]]:
    """
    Sorts drivers based on their performance scores in descending order.

    Args:
        race_scores: Dictionary with driver names as keys and scores as values.

    Returns:
        list: Sorted list of tuples (name, score) from highest to lowest.
    """
           
    final_ranking = sorted(race_scores.items(), key=lambda item: item[1], reverse=True)
    
    return final_ranking


# ----------------------------
# 3. MAIN FLOW FUNCTIONS
# ----------------------------

def choose_driver(available_drivers: list[dict[str, int]]) -> dict[str, int]:
    """
    Displays available drivers and handles user selection via terminal input.

    Args:
        available_drivers: List of driver dictionaries containing 'name', 'skill', etc.

    Returns:
        dict: The dictionary of the driver selected by the user.
    """

    print("--- DRIVER SELECTION ---")
    print("Available drivers for this season:")
    for index, driver in enumerate(available_drivers, start=1):
        print(f'{index}- {driver["name"]}')

    while True:
        try:
            choice = int(input("\nSelect your driver (1-3): "))
            if 1 <= choice  <= len(available_drivers):
                selected_driver = available_drivers[choice-1]
                    
                print(f"\n>>> Confirmed: You are racing as {selected_driver['name']}!")
                return selected_driver
                
            else:
                print(f"Error: Please choose a number between 1 and {len(available_drivers)}.")
           

        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            

def run_championship(available_drivers: list[dict[str, int]], available_tracks: list[dict[str, float]]) -> dict[str, int]:
    """
    Orchestrates the championship by running races on all available tracks.

    Args:
        available_drivers: List of driver dictionaries.
        available_tracks: List of track dictionaries.

    Returns:
        dict: A dictionary containing the accumulated points for each driver.
    """

    overall_standings = {driver["name"]: 0 for driver in available_drivers} 
    
    print("\n" + "="*40)
    print("THE CHAMPIONSHIP SEASON BEGINS NOW!")
    print("="*40)
    input("Press ENTER to continue.\n")

 
    for i, track in enumerate(available_tracks, start=1):

        print(f"\nROUND {i} of {len(available_tracks)}")
        print(f"LOCATION: {track['name']}")
        print("-" * 20)
         
        input(f"Press ENTER to start the {track['name']} Grand Prix!")
  
        # Execute the race simulation
        race_ranking = run_race(available_drivers, track)

        print(f'\n--- RACE RESULTS: {track["name"].upper()} ---')
        
        for position, result in enumerate(race_ranking, start=1):
            driver_name = result[0]
            points = POINTS_SYSTEM[position]
            print(f'{position}º Place: {driver_name} (+{points} pts)')      
            
            # Update the global standings using the points system
            overall_standings[driver_name] += points       
                      
        current_classification = sorted(overall_standings.items(), key=lambda item: item[1], reverse=True)
        
        print("\n--- CURRENT WORLD STANDINGS ---")
        for rank, driver_data in enumerate(current_classification, start=1):
            print(f"{rank}º {driver_data[0]}: {driver_data[1]} pts")

        if i < len(available_tracks):
            input("\nPress ENTER to travel to the next circuit...")
        else:
            print("\nFinal race of the season completed!")
            input("Press ENTER to see the final championship verification...")

    """
    # --- DEBUG SECTION ---
    # Toggle these variables to test different tie scenarios
    TEST_TRIPLE_TIE = True
    TEST_DUAL_TIE = True 

    if TEST_TRIPLE_TIE:
        print("\n" + "!" * 40)
        print("DEBUG: FORCING A TRIPLE TIE (ALL DRIVERS)")
        for driver in available_drivers:
            overall_standings[driver["name"]] = 100
        print("!" * 40 + "\n")

    elif TEST_DUAL_TIE:
        # Sort current standings to find who the top 2 are
        temp_standings = sorted(overall_standings.items(), key=lambda item: item[1], reverse=True)
        leader_1 = temp_standings[0][0]
        leader_2 = temp_standings[1][0]
        
        print("\n" + "!" * 60)
        print(f"DEBUG: FORCING A DUAL TIE BETWEEN {leader_1} AND {leader_2}")
        overall_standings[leader_1] = 100
        overall_standings[leader_2] = 100
        # Ensure the 3rd place is lower
        if len(temp_standings) > 2:
            overall_standings[temp_standings[2][0]] = 50
        print("!" * 60 + "\n")
    
    # Refresh the classification after debug manipulation
    current_classification = sorted(overall_standings.items(), key=lambda item: item[1], reverse=True)
    # --- END DEBUG SECTION ---
    """
    
    final_standings_list = list(current_classification)
    highest_score = max(score for name, score in final_standings_list)  
    
    # Identify all drivers who share the top score
    tied_leaders = [driver for driver in final_standings_list if driver[1] == highest_score]
    
    if len(tied_leaders) == 1:
        return overall_standings
        
    else:
        print("\n" + "!"*40)
        print("DRAMA! THE CHAMPIONSHIP ENDED IN A TIE!")
        print(f"A winner-takes-all tie-breaker will be held at {EXTRA_TIE_TRACK['name']}!")
        print("!"*40)
        
        tied_driver_names = [driver[0] for driver in tied_leaders]
        contending_drivers = [driver for driver in available_drivers if driver["name"] in tied_driver_names]
        
        input("\nPress ENTER to start the SUDDEN DEATH FINAL...")
        tie_breaker_results = run_race(contending_drivers, EXTRA_TIE_TRACK)
        
        
        print(f"--- TIE-BREAKER FINISHED! ---\n")
        winner_name = tie_breaker_results[0][0]
        print(f'THE CHAMPION IS DECIDED: {winner_name} wins the tie-breaker!')
        
        # Reset standings to mark tie-breaker winner (flag-based result)
        overall_standings = {driver["name"]: 0 for driver in available_drivers}
        overall_standings[winner_name] = 1 # Flag value for tie-breaker victory
    
    return overall_standings
    
        
def display_final_results(championship_results: dict[str, int], player_driver: dict[str, int]) -> None:
    """
    Identifies the champion and displays the final message to the user.

    Args:
        championship_results: Dictionary with final points or tie-breaker flag.
        player_driver: The driver dictionary the user chose.
    """

    final_ranking = sorted(championship_results.items(), key=lambda item: item[1], reverse=True)
   
    winner_name, winner_points = final_ranking[0]
    player_driver_name = player_driver["name"]
    
    print("\n" + "*" * 40)
    print("       FINAL SEASON SUMMARY")
    print("*" * 40)
  
    if winner_name == player_driver_name:
        print(f"🏆 WORLD CHAMPION: {player_driver_name} 🏆")
        print("Incredible performance! You've reached the top of the podium!")
        if winner_points == 1:
            print(f"Victory secured in the intense FINAL TIE-BREAKER!")
        

    else:    
        print(f"RANKING: Your driver, {player_driver_name}, finished behind the leader.")
        print(f"The title goes to {winner_name}!")
        if winner_points == 1:
            print(f"{winner_name} took the crown in the FINAL TIE-BREAKER!")
        
        print("Better luck next season. Keep practicing!")

    print("*" * 40 + "\n")

# ----------------------------
# 4. MAIN
# ----------------------------

def main():   
    """
    Main execution entry point. 
    Manages the overall flow of the F1 Simulation from welcome to final results.
    """   
    print("=" * 50)    
    print("      FORMULA 1 SEASON SIMULATOR - V1")
    print("=" * 50)
    print("\nHOW IT WORKS:")
    print(f"- You will compete in a short season of {len(TRACKS)} races.")
    print("- Drivers earn points based on their finishing position (25, 18, 15).")
    print("- The driver with the most points after the final race wins the title.")
    print("- In case of a draw, a 'Sudden Death' race at Nürburgring will decide the Champion.")
    print("-" * 50 + "\n")
   

   
    # 1. Setup: User chooses their driver
    selected_driver = choose_driver(DRIVERS)    
    
    # 2. Simulation: Run all races in the season
    final_standings = run_championship(DRIVERS, TRACKS)
    
    # 3. Conclusion: Determine and display the champion
    display_final_results(final_standings, selected_driver)
    
    

if __name__ == "__main__":
    main()