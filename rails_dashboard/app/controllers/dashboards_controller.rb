require 'open-uri'
class DashboardsController < ApplicationController
	def test
		#@data = IO.read("/home/honu/projects/twitter/fallout4_json.txt").to_s
		#@data = JSON.parse(open("http://localhost:5000/words_cloud_test_json").read)
		@data = open("http://localhost:5000/words_cloud_test_json").read
	end


	def test_json
		@data = open("http://localhost:5000/words_cloud_test_json").read
		render json: @data
	end

	def index
		@data = open("http://localhost:5000/words_cloud_test_json").read
		render layout: 'dashboard_layout'
	end



end
