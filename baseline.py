import pandas as pd
import numpy as np

def base_evaluating(test_user_data, user_indexed_reviews, restaurant_indexed_reviews):
	evaluations = dict()

	avg_star = cal_average_rating(user_indexed_reviews)

	user_avg = cal_user_avg(user_indexed_reviews)
	biz_avg = cal_restaurant_avg(restaurant_indexed_reviews)

	for user in test_user_data:
		#evaluations[user] = dict()
		ustars = float(user_avg[user])
		for restaurant, rating in test_user_data[user].items():
			bstars = float(biz_avg[restaurant])
			true = rating
			pair = (user, restaurant)
			prediction = avg_star + (bstars - avg_star) + (ustars - avg_star)
			evaluations[pair] = (prediction, true)
	return evaluations

def cal_average_rating(user_indexed_reviews):
    """
    calculate average rating for the whole training dataset
    """
    total = 0.
    count = 0
    for user in user_indexed_reviews:
    	for restaurant, rating in user_indexed_reviews[user].items():
    		total += rating
    		count += 1
    return total/count

def cal_user_avg(user_indexed_reviews):
	"""
	calculate average rating of each user
	"""
	user_avg = dict()
	for user in user_indexed_reviews:
		total = 0.
		count = 0
		for restaurant, rating in user_indexed_reviews[user].items():
			total += rating
			count += 1
		user_avg[user] = total/count
	return user_avg

def cal_restaurant_avg(restaurant_indexed_reviews):
	"""
	calculate average rating of each restaurant
	"""
	biz_avg = dict()
	for restaurant in restaurant_indexed_reviews:
		total = 0.
		count = 0
		for user, rating in restaurant_indexed_reviews[restaurant].items():
			total += rating
			count += 1
		biz_avg[restaurant] = total/count
	return biz_avg

