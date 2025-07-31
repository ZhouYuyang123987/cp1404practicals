# import datetime
#
# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))


incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    if incomplete:
        print("Incomplete projects:")
        for project in sorted(incomplete):
            print(f"  {project}")
    else:
        print("No incomplete projects.")

    if complete:
        print("Completed projects:")
        for project in sorted(complete):
            print(f"  {project}")
    else:
        print("No completed projects.")