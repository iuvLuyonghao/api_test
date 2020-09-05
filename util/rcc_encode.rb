#!/Users/alex/.rbenv/shims/ruby

require 'openssl'
require 'base64'

def encoder
  # return @@des if @@des.present?
  des = OpenSSL::Cipher.new('aes-256-ctr')
  des.encrypt
  des.key = ARGV[1]
  des.iv = ARGV[2]
  des
end

def new_tt
  t = Time.now.strftime("%Y-%m-%d %H:%M:%S")
  json = t
  result = encoder.update(json)
  result << encoder.final
  r = Base64.encode64 result
  puts t, r
end
new_tt