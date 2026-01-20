def view_sessions(sessions):
    if not sessions:
        print("No training sessions recorded.")
        return

    print("\n=== Training History ===")
    for session in sessions:
        print(session)
