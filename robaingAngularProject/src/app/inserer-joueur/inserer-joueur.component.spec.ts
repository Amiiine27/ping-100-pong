import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsererJoueurComponent } from './inserer-joueur.component';

describe('InsererJoueurComponent', () => {
  let component: InsererJoueurComponent;
  let fixture: ComponentFixture<InsererJoueurComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InsererJoueurComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InsererJoueurComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
