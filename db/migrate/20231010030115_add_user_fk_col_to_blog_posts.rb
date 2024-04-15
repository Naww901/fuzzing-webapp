class AddUserFkColToBlogPosts < ActiveRecord::Migration[7.0]
  def change
    add_reference :blog_posts, :user, foreign_key: true
  end
end
