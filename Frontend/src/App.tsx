import React from 'react';
import './App.css';
import Photos from "./admin/Photos";
import {BrowserRouter, Route} from "react-router-dom";
import Main from "./main/Main";
import PhotosCreate from "./admin/PhotosCreate";
import PhotosEdit from "./admin/PhotosEdit";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Route path='/' exact component={Main}/>
                <Route path='/admin/photos' exact component={Photos}/>
                <Route path='/admin/photos/create' exact component={PhotosCreate}/>
                <Route path='/admin/photos/:id/edit' exact component={PhotosEdit}/>
            </BrowserRouter>

        </div>
    );
}

export default App;
