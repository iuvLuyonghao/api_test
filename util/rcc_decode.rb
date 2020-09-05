#!/usr/bin/env ruby

require 'openssl'
require 'base64'

data = Base64.decode64(ARGV[0])
aes = OpenSSL::Cipher::Cipher.new("aes-256-ctr")
aes.decrypt
aes.key = ARGV[1]
aes.iv = ARGV[2]
result = aes.update(data) << aes.final
puts result

