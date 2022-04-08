if ARGV.length < 2
    puts "Usage: HelloGoodbye.rb name-1 name-2"
    exit
else
    puts "Hello #{ARGV[0]} and #{ARGV[1]}"
    puts "Goodbye #{ARGV[1]} and #{ARGV[0]}"
end