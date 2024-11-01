from exercise import Exercise
from workout import Workout
from progress import ProgressTracker
from user import User
import datetime


def get_string_input(input_prompt: str):
    while True:
        input_string = input(input_prompt).strip()
        if not input_string:
            print('Input cannot be empty.')
        else:
            return input_string


def get_integer_input(input_prompt: str):
    while True:
        try:
            return int(input(input_prompt).strip())
        except ValueError:
            print('Please enter a valid integer number.')


def get_float_input(input_prompt: str):
    while True:
        try:
            return float(input(input_prompt).strip())
        except ValueError:
            print('Please enter a valid number.')


def get_menu_input(input_prompt: str, menu_name: list):
    while True:
        try:
            menu_input = int(input(input_prompt).strip())
            if 1 <= menu_input <= len(menu_name):
                return menu_input
            else:
                print(f'Please input a valid number from 1 to {len(menu_name)}.')
        except ValueError:
            print('Please enter a valid number.')


print('Welcome to the Fitness Tracking app!\nIn order to create a new user, we will need the following:')

logged_user = User(get_string_input('Your name: '), get_integer_input('Your age: '), get_float_input('Your weight: '),
                   get_float_input('Your height: '), get_string_input('Your goal: '))

squats = Exercise('Squats', 'Leg Exercise', 'High')
deadlifts = Exercise('Deadlifts', 'Full Body Exercise', 'High')
bench_press = Exercise('Bench Press', 'Push Exercise', 'Low')
push_ups = Exercise('Push Ups', 'Push Exercise', 'Low')
lunges = Exercise('Lunges', 'Leg Exercise', 'Medium')

exercise_list = [squats, deadlifts, bench_press, push_ups, lunges]

full_body_routine = Workout('Full Body Routine')
full_body_routine.add_exercise('Bench Press', 3, 12, 120, True)
push_day_routine = Workout('Push Day Routine')
push_day_routine.add_exercise('Push Ups', 2, 16, 80, True)
pull_day_routine = Workout('Pull Day Routine')
pull_day_routine.add_exercise('Deadlifts', 5, 8, 240, True)
leg_day_routine = Workout('Leg Day Routine')
leg_day_routine.add_exercise('Squats', 3, 12, 120, True)
leg_day_routine.add_exercise('Lunges', 3, 12, 120, True)

routine_list = [full_body_routine, pull_day_routine, pull_day_routine, leg_day_routine]

print(f'Hello, {logged_user.name}! Thank you for setting up your profile!')

main_menu = ['Profile', 'Exercises', 'Workouts', 'Progress', 'Exit']

while True:

    for index, menu_option in enumerate(main_menu, 1):
        print(f"{index}. {menu_option}")

    user_input = get_menu_input('Please select one of the options by inputting its number: ', main_menu)

    if user_input == 1:
        # Profile submenu
        while True:

            profile_menu = ['View Profile', 'Edit Profile', 'Go Back']
            for index, menu_option in enumerate(profile_menu, 1):
                print(f"{index}. {menu_option}")
            user_input = get_menu_input('Please select one of the options by inputting its number: ', profile_menu)

            if user_input == 1:
                # Display User Info
                print(logged_user.display_info())

            elif user_input == 2:
                # Edit Profile
                edit_profile_menu = ['Change Weight', 'Change Goal']
                for index, edit_menu_item in enumerate(edit_profile_menu, 1):
                    print(f'{index}. {edit_menu_item}')
                user_input = get_menu_input('Please select one of the options by inputting its number: ',
                                            edit_profile_menu)
                if user_input == 1:
                    # Change Weight
                    new_weight = get_float_input('Please input your new weight:')
                    logged_user.weight = new_weight
                    print(f'Your new weight is {logged_user.weight:.2f}.')
                elif user_input == 2:
                    # Change Goal
                    new_goal = get_string_input('Please input your new goal: ')
                    logged_user.goal = new_goal
                    print(f'Your new goal is {logged_user.goal}.')
                elif user_input == 3:
                    break

    elif user_input == 2:
        # Exercise submenu
        while True:

            exercise_menu = ['View Exercises', 'Add Exercise To App Database', 'Remove Exercise From App Database',
                             'Go Back']
            for index, menu_option in enumerate(exercise_menu, 1):
                print(f"{index}. {menu_option}")
            user_input = get_menu_input('Please select one of the options by inputting its number: ', exercise_menu)
            if user_input == 1 or user_input == 3:
                # View Exercises/Remove Exercise From Database
                for index, exercise in enumerate(exercise_list, 1):
                    print(f'{index}. ' + exercise.display_exercise())
                if user_input == 1:
                    print(f'{len(exercise_list)} exercises available in total.')
                elif user_input == 3:
                    remove_exercise_position = get_menu_input(
                        'Please input the number of the exercise you wish to be removed: ', exercise_list) - 1
                    print(
                        f'{exercise_list[remove_exercise_position].name} has been removed from the exercise database.')
                    exercise_list.pop(remove_exercise_position)

            elif user_input == 2:
                # Add Exercise To Database
                exercise_name = get_string_input('Please input the name of the exercise: ')
                duplicate_exercise = False
                for exercise in exercise_list:
                    if exercise.name.lower() == exercise_name.lower():
                        print('The exercise is already in the app database.')
                        duplicate_exercise = True
                        break
                if not duplicate_exercise:
                    exercise_difficulty = get_string_input('Please input the difficulty of the exercise: ')
                    exercise_description = get_string_input('Please input the description of the exercise: ')
                    exercise_list.append(Exercise(exercise_name, exercise_description, exercise_difficulty))
                    print(f'Exercise {exercise_name} has been added to the exercise database.')
            elif user_input == 4:
                break

    elif user_input == 3:
        # Workouts submenu
        while True:

            workout_menu = ['View Available Workout Routines', 'Create A Workout Routine', 'Modify A Workout Routine',
                            'Delete A Workout Routine', 'Go Back']
            for index, menu_option in enumerate(workout_menu, 1):
                print(f"{index}. {menu_option}")
            user_input = get_menu_input('Please select one of the options by inputting its number: ', workout_menu)

            if user_input == 1:
                # View Workout
                for index, routine_option in enumerate(routine_list, 1):
                    print(f'{index}. Workout: {routine_option.name}')
                user_input = get_menu_input('Please select which workout you wish to view by inputting its number: ',
                                            routine_list) - 1
                routine_list[user_input].view_workout()

            elif user_input == 2:
                # Create Workout
                user_input = get_string_input('Please input the name of the new workout: ')
                duplicate_workout = False
                for routine in routine_list:
                    if routine.name.lower() == user_input.lower():
                        print('Invalid input. A workout with that name already exists.')
                        duplicate_workout = True
                        break
                if not duplicate_workout:
                    routine_list.append(Workout(user_input))
                    print(f'Workout {user_input} has been added to the database.')

            elif user_input == 3:
                # Modify Workout
                for index, routine_option in enumerate(routine_list, 1):
                    print(f'{index}. Workout: {routine_option.name}')
                user_input = get_menu_input('Please select which workout you wish to modify by inputting its number: ',
                                            routine_list) - 1
                workout_index = user_input
                print(f'Now modifying {routine_list[workout_index].name} workout.')

                modify_workout_menu = ['Add Exercise', 'Remove Exercise', 'Go Back']
                for index, menu_option in enumerate(modify_workout_menu, 1):
                    print(f'{index}. {menu_option}')
                user_input = get_menu_input('Please select which action you wish to take by inputting its number: ',
                                            modify_workout_menu)
                if user_input == 1:
                    # Add Exercise To Workout
                    for index, exercise in enumerate(exercise_list, 1):
                        print(f'{index}, {exercise.name}')
                    user_input = get_menu_input(
                        'Please select which exercise you wish to add by inputting its number: ',
                        exercise_list) - 1
                    exercise_name = exercise_list[user_input].name

                    input_sets = get_integer_input('Please enter the number of sets: ')
                    input_reps = get_integer_input('Please enter the number of reps: ')
                    input_rest_time = get_integer_input('Please enter the rest time: ')

                    routine_list[workout_index].add_exercise(exercise_name, input_sets, input_reps, input_rest_time)

                elif user_input == 2:
                    # Remove Exercise From Workout
                    routine_list[workout_index].view_workout()
                    user_input = get_menu_input(
                        'Please select which exercise you wish to remove by inputting its number: ',
                        exercise_list) - 1
                    exercise_name = routine_list[workout_index].exercises[user_input]['exercise']
                    routine_list[workout_index].remove_exercise(exercise_name)
                elif user_input == 3:
                    # Go Back
                    break

            elif user_input == 4:
                # Delete Workout
                for index, routine_option in enumerate(routine_list, 1):
                    print(f'{index}. Workout: {routine_option.name}')
                user_input = get_menu_input('Please select which workout you wish to delete by inputting its number: ',
                                            routine_list) - 1
                print(f'Workout {routine_list[user_input].name} has been deleted.')
                routine_list.pop(user_input)

            elif user_input == 5:
                # Go Back
                break

    elif user_input == 4:
        # Progress submenu
        progress_menu = ['Log Workout Session', 'Generate Report', 'Go Back']
        for index, menu_option in enumerate(progress_menu, 1):
            print(f'{index}. {menu_option}')
        user_input = get_menu_input('Please select which action you wish to take by inputting its number: ',
                                    progress_menu)
        progress_object = ProgressTracker(logged_user)

        if user_input == 1:
            # Log Workout Session
            for index, routine_option in enumerate(routine_list, 1):
                print(f'{index}. Workout: {routine_option.name}')
            user_input = get_menu_input('Please select which workout to add to the tracker by inputting its number: ',
                                        routine_list) - 1
            workout_index = user_input
            print(
                f'Logged {routine_list[workout_index].name} workout at {datetime.datetime.now().strftime("%H:%M %d.%m.%y")}.')
            progress_object.log_workout(routine_list[workout_index].name)

        elif user_input == 2:
            # Generate Report
            print(progress_object.generate_report())

        elif user_input == 3:
            # Go Back
            break


    elif user_input == 5:
        # Exit
        exit()
