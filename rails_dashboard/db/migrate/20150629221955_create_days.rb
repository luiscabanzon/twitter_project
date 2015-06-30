class CreateDays < ActiveRecord::Migration
  def change
    create_table :days do |t|
      t.string :date
      t.text :topics

      t.timestamps null: false
    end
  end
end
