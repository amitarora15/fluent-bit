function modify_logs(tag, timestamp, record)
  local tag_index = {
    fluent_logs = "fluent_log",
    my_log = "app_logs"
  }
  new_record = record
  new_record["index_name"] = tag_index[tag]
  return 1, timestamp, new_record
end
