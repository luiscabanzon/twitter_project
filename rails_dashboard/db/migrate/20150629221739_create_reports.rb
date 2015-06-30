class CreateReports < ActiveRecord::Migration
  def change
    create_table :reports do |t|
      t.string :date
      t.string :trend
      t.text :data

      t.timestamps null: false
    end
  end
end
