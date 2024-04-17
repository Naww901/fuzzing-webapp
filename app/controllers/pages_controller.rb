class PagesController < ApplicationController

    ALLOWED_IMAGE_EXTENSIONS = %w[jpg jpeg gif png bmp].freeze

    def index
        render :welcome
    end

    def create
        uploaded_file = params[:file_upload]
        
        if uploaded_file && image_extension_allowed?(uploaded_file.original_filename)
        dir = Rails.root.join('public', 'uploads')
        FileUtils.mkdir_p(dir) unless Dir.exist?(dir)
        
        file_path = dir.join(uploaded_file.original_filename)
        
        File.open(file_path, 'wb') do |file|
            file.write(uploaded_file.read)
        end
        
        # Redirect with a success message only if the file is allowed and saved
        redirect_to welcome_page_path, notice: "File uploaded successfully."
        else
        # If the file is not allowed, redirect with an error message
        redirect_to welcome_page_path, alert: "File type not allowed."
        end
        
        rescue StandardError => e
            redirect_to welcome_page_path, alert: "File upload failed: #{e.message}"
    end

    def ror
        render :ror
    end

    def about
        render :about
    end

    def fuzzing
        render :fuzzing
    end

    def image_extension_allowed?(filename)
        extension = File.extname(filename).delete('.').downcase
        ALLOWED_IMAGE_EXTENSIONS.include?(extension)
    end


end
