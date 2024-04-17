# frozen_string_literal: true

Rails.application.routes.draw do
  devise_for :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
  root to: redirect('welcome')

  get 'welcome', to: 'pages#index', as: 'welcome_page'
  post '/upload', to: 'pages#create'

  get 'ror', to: 'pages#ror', as: 'ror_page'
  get 'about', to: 'pages#about', as: 'about_page'
  get 'fuzzing', to: 'pages#fuzzing', as: 'fuzzing_page'

end
