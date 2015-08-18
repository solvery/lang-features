
for k,v in pairs(_G) do 
  print(string.format("%s => %s","_G." .. k,v))
  if type(v) == "table" and k ~= "_G" then
     for key in pairs(v) do
        print("  " .. k .. "." .. key) --为了便于阅读，进行了特殊格式化处理
     end
  end
end

