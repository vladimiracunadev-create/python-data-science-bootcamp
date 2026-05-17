/**
 * AppNavigator.js — Configuracion de rutas de la app
 *
 * Rutas disponibles:
 *   Home       → Lista de los 13 módulos con progreso
 *   Class      → Detalle de una clase (teoría + ejercicios + Colab)
 */

import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../screens/HomeScreen';
import ClassScreen from '../screens/ClassScreen';

const Stack = createStackNavigator();

// Opciones de header compartidas por todas las pantallas
const headerOptions = {
  headerStyle: {
    backgroundColor: '#1a1a2e',   // fondo del header
    elevation: 0,                  // sin sombra en Android
    shadowOpacity: 0,              // sin sombra en iOS
    borderBottomWidth: 1,
    borderBottomColor: '#334155',  // linea separadora sutil
  },
  headerTintColor: '#f1f5f9',       // color de titulos e iconos
  headerTitleStyle: {
    fontWeight: '700',
    fontSize: 17,
  },
  headerBackTitleVisible: false,    // ocultar texto "Atrás" en iOS
};

export default function AppNavigator() {
  return (
    <Stack.Navigator
      initialRouteName="Home"
      screenOptions={headerOptions}
    >
      {/* Pantalla principal: lista de clases */}
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{ title: 'Bootcamp Python DS' }}
      />

      {/* Pantalla de clase: el titulo se asigna dinamicamente en ClassScreen */}
      <Stack.Screen
        name="Class"
        component={ClassScreen}
        options={({ route }) => ({
          title: route.params?.classTitle ?? 'Clase',
        })}
      />
    </Stack.Navigator>
  );
}
