def add_session(sessions):
    date = input("Enter date (YYYY-MM-DD): ")
    activity = input("Enter activity type: ")

    duration = int(input("Enter duration (minutes): "))
    intensity = int(input("Enter intensity (1-5): "))

    session = TrainingSession(date, activity, duration, intensity)
    sessions.append(session)

    print("Training session added successfully.")
