
-- 基于递归的实现版本

function re_print(t,prefix)
  for k,v in pairs(t) do
    if type(v) == "string" then
      print(string.format("%s => %s", prefix .. "." .. k,v))
    else
      print(prefix .. "." .. k)
    end
    if type(v) == "table" and k ~= "_G" and k ~= "_G._G" and not v.package then
      re_print(v, "  " .. prefix .. "." .. k)
    end
  end
end
