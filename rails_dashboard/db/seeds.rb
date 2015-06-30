# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
reports = Dir["/home/honu/projects/tweetpeek/db/json/*"]
reports.each do |file| {
	Report.create(date: file[38,10], trend: file[49,(file.length-58)], data: File.read(file))
}

topics = Dir["/home/honu/projects/tweetpeek/db/trends/*"]
topics.each do |topic| {
	Day.create(date: topic[40,10], topics: File.read(topic))
}