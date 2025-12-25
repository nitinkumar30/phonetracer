def main():
    print("""
PhoneTracer v2.3
----------------
1. Argument mode
2. Command-line menu
3. GUI
4. Exit
""")

    choice = input("Choose mode: ").strip()

    if choice == "1":
        import cli_args
        cli_args.run()

    elif choice == "2":
        import cli_menu
        cli_menu.run()

    elif choice == "3":
        import gui_app
        gui_app.run()

    else:
        print("Exiting")

if __name__ == "__main__":
    main()
