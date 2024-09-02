require 'heapq'
require 'set'

n, k = gets.split.map(&:to_i)

array = n.times.map do
  t, b = gets.split.map(&:to_i)
  [b, t]  # Store as [b, l]
end

array.sort!

base = array.shift

# Use a max-heap by negating the length
heap = array.map.with_index { |(b, l), i| [-l, b, i] }
heapq = Heapq.new(heap)

hash_map = Hash.new(0)
total = base[1]

(k - 1).times do
  break if heapq.empty?

  l, b, _ = heapq.heappop
  total += -l
  hash_map[[-l, b]] += 1
end

ans = base[0] * total
total -= base[1]

array.each_with_index do |(b, l), i|
  if hash_map[[-l, b]] > 0
    hash_map[[-l, b]] -= 1
    hash_map.delete([-l, b]) if hash_map[[-l, b]] == 0

    until heapq.empty?
      c, d, index = heapq.heappop
      next if index < i

      hash_map[[c, d]] += 1
      total += -c
      break
    end
  else
    total += l
  end

  ans = [ans, total * b].max
  total -= l
end

puts ans
