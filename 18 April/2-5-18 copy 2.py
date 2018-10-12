# import os
# import datetime
# cwd = os.getcwd()
# # print(os.listdir())
# # c_time = os.stat('testEmployee.db').st_ctime
# # c_time = datetime.date.fromtimestamp(c_time)
# # print(c_time)

# for item in os.listdir():
#     c_time = os.stat(item).st_ctime
#     c_time = datetime.date.fromtimestamp(c_time)
#     c_time = str(c_time)
#     if not os.path.exists(c_time):
#         os.makedirs(c_time)
#     new_path = os.path.join(c_time, item)
#     os.rename(item, new_path)
