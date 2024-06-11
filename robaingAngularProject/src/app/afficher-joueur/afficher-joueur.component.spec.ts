import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AfficherJoueurComponent } from './afficher-joueur.component';

describe('AfficherJoueurComponent', () => {
  let component: AfficherJoueurComponent;
  let fixture: ComponentFixture<AfficherJoueurComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AfficherJoueurComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AfficherJoueurComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
