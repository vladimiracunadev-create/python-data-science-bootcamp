/**
 * App.js — Punto de entrada de la app Bootcamp Python DS
 *
 * Configura:
 *   - NavigationContainer con tema oscuro
 *   - Stack Navigator con las pantallas principales
 *   - SafeAreaProvider para respetar notches y barras del sistema
 */

import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { NavigationContainer, DarkTheme } from '@react-navigation/native';
import AppNavigator from './src/navigation/AppNavigator';

// Tema oscuro personalizado para la navegacion
const BootcampTheme = {
  ...DarkTheme,
  colors: {
    ...DarkTheme.colors,
    primary: '#22c55e',      // verde — color de accion principal
    background: '#0f0f1a',   // fondo oscuro azulado
    card: '#1a1a2e',         // fondo de tarjetas y headers
    text: '#f1f5f9',         // texto principal claro
    border: '#334155',       // bordes sutiles
    notification: '#22c55e', // badges de notificacion
  },
};

export default function App() {
  return (
    <SafeAreaProvider>
      {/* StatusBar: iconos blancos sobre fondo oscuro */}
      <StatusBar style="light" backgroundColor="#0f0f1a" />

      {/* NavigationContainer: envuelve toda la navegacion de la app */}
      <NavigationContainer theme={BootcampTheme}>
        <AppNavigator />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
