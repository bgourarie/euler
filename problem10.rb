# I took a brief foray into Ruby in preparation for a new project at work. I used this problem to practice initially. 
# shoutout to why's poignant guide to ruby :-)

module Euler10
	def self.sieve(num)
		sieve = []
		for i in 2 .. num
			sieve[i] = i
		end
		for i in 2 .. Math.sqrt(num)
			next unless sieve[i]
			(i*i).step(num, i) do |j|
				sieve[j] = nil
			end
		end
		sieve.compact
	end
	primes = sieve(2_000_000)
	sum = primes.inject { |sum,n| sum + n }
	p sum
end
