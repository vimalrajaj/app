/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert } from 'react-native';

export default function App() {
  const [task, setTask] = useState('');
  const [limit, setLimit] = useState('');

  return (
    <View style={{ padding: 60, justifyContent: 'center' }}>
      <Text style={{fontSize: 22, fontWeight: 'bold', marginBottom: 20}}>Task Timer</Text>
      <TextInput placeholder="Task Name" onChangeText={setTask} style={{borderBottomWidth: 1, marginBottom: 15}} />
      <TextInput placeholder="Time Limit (e.g. 30 mins)" onChangeText={setLimit} style={{borderBottomWidth: 1, marginBottom: 30}} />
      <Button title="Set Deadline" onPress={() => Alert.alert("Timer Set", `Task: ${task}\nLimit: ${limit}`)} />
    </View>
  );
}