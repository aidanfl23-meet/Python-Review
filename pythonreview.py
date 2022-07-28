title = input ("Enter Video Title")
description = input ("Enter Video Description")
username = input ("Enter Username")
comment = input("Enter Comment")

def create_youtube_video (title, description):
	dict1 = { "title" : title , "Description" : description , "Like" : 0 , "Dislike" : 0, "Comments" : {} }
	return dict1

def like (youtube_video):
	if "Like" in youtube_video:
		youtube_video ["Like"] += 1
	return youtube_video


def dislike (youtube_video):
	if "Dislike" in youtube_video:
		youtube_video ["Dislike"] += 1
	return youtube_video

def add_comment (youtube_video, username, comment):
	youtube_video ["Comments"][username] = comment
	return youtube_video


youtube_video = create_youtube_video (title, description)
youtube_video = like(youtube_video)
youtube_video = dislike(youtube_video)
youtube_video = add_comment(youtube_video, username, comment)
print (youtube_video)
