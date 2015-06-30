require 'open-uri'
class DashboardsController < ApplicationController
	def index
		@data = open("http://localhost:5000/words_cloud_test_json").read
		render layout: 'dashboard_layout'
	end

	def api
		@data = JSON.parse(open("http://localhost:5000/api/" + params[:date] + "_" + params[:topic]).read)
		render 'index', layout: 'dashboard_layout'
	end

	def json
		@data = JSON.parse(open("http://localhost:5000/api/" + params[:date] + "_" + params[:topic]).read)
		render json: @data
	end

	def test2
		@data = open("http://localhost:5000/test2").read
		render 'index', layout: 'dashboard_layout'
	end

	def test
		#@data = IO.read("/home/honu/projects/twitter/fallout4_json.txt").to_s
		#@data = JSON.parse(open("http://localhost:5000/words_cloud_test_json").read)
		@data = open("http://localhost:5000/words_cloud_test_json").read
	end

	def test2
		@data = open("http://localhost:5000/test2").read
		render 'index', layout: 'dashboard_layout'
	end

	def test_json
		@data = open("http://localhost:5000/words_cloud_test_json").read
		render json: @data
	end


end
