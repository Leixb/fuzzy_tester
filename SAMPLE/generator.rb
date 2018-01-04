#!/usr/bin/ruby
Cards = "AKQJTN"

def my_test()
    (0...5).map { (Cards[rand(6)]) }.join \
    << ' ' \
    << (0...5).map { (Cards[rand(6)]) }.join \
    << "\n"
end

(rand(10) + 2).times do
    print my_test
end

