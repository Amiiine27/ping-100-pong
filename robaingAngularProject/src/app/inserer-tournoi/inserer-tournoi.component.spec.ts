import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsererTournoiComponent } from './inserer-tournoi.component';

describe('InsererTournoiComponent', () => {
  let component: InsererTournoiComponent;
  let fixture: ComponentFixture<InsererTournoiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InsererTournoiComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InsererTournoiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
