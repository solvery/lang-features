
-- Lua也是用Table来管理全局变量的，Lua把这些全局变量放在了一个叫“_G”的Table里。

-- for k, v in pairs(_G) do
for k, v in pairs(_G.os) do
    print(k)
end

